import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    """
    A configuration class that retrieves env variables and stores config settings.
    """

    HOSTED_BASE_URL = os.getenv("HOSTED_BASE_URL")
    HOSTED_API_KEY = os.getenv("HOSTED_API_KEY")
    LOCAL_BASE_URL = os.getenv("LOCAL_BASE_URL")

    AVAILABLE_MODELS = [
        "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
        "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        "llama3.1",
    ]