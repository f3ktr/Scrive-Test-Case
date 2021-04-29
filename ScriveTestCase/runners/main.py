from stepDefinitions import DocuSignStepDefs
from utilities import ConfigurationReader

chrome = ConfigurationReader.config.get("BROWSER","chrome")
firefox = ConfigurationReader.config.get("BROWSER","firefox")

DocuSignStepDefs.verify_that_document_signed(browser = firefox, sendingName="Faruk")

DocuSignStepDefs.verify_that_document_signed(browser = chrome, sendingName="Faruk E")