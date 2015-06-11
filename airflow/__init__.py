"""
Authentication is implemented using flask_login and different environments can
implement their own login mechanisms by providing an `airflow_login` module
in their PYTHONPATH. airflow_login should be based off the
`airflow.www.login`
"""
__version__ = "1.0.1"

import logging
from airflow.configuration import conf
from airflow.models import DAG
from flask.ext.admin import BaseView


from airflow import default_login as login
if conf.getboolean('webserver', 'AUTHENTICATE'):
    try:
        # Environment specific login
        import airflow_login as login
    except ImportError:
        logging.error(
            "authenticate is set to True in airflow.cfg, "
            "but airflow_login failed to import")


class PluginView(BaseView):
    pass

from airflow import operators
from airflow import hooks
from airflow import executors

operators.integrate_plugins()
hooks.integrate_plugins()
