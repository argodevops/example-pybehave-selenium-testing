from pybehave.features.environment import before_all as pybehave_before_all
from pybehave.features.environment import before_scenario as pybehave_before_scenario
from pybehave.features.environment import after_all as pybehave_after_all

import logging


def before_all(context):
    """Custom before_all that extends pybehave default behavior."""
    logging.info("Custom before_all: Example app is initialising.")
    pybehave_before_all(context)

    context.example_app_config = {"custom_key": "custom_value"}
    logging.info("Custom before_all: Example app config added: %s", context.example_app_config)


def before_scenario(context, scenario):
    """Custom before_scenario that extends pybehave default behavior."""
    logging.info("Custom before_scenario: Preparing for scenario.")
    pybehave_before_scenario(context, scenario)

    if "custom_tag" in scenario.effective_tags:
        logging.info("Custom scenario tag detected: custom_tag")


def after_all(context):
    """Custom after_all that extends pybehave default behavior."""
    logging.info("Custom after_all: Cleaning up after all tests.")
    pybehave_after_all(context)

    logging.info("Custom cleanup completed.")
