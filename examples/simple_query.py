import setup
import cdcwonderpy as wonder
from cdcwonderpy.enums import *

"""
    Example of a query that shows how simple it is to get the most general
    version of the data. No need to specify the parameters you don't care about.
    
    Here, we want to get all the American Indian/Alaskan Native deaths grouped by year and view
    the result as a Pandas dataframe.
    """
response = wonder.Request().race(Race.AMERICAN_INDIAN_OR_ALASKAN_NATIVE).send()
print(response.as_dataframe())