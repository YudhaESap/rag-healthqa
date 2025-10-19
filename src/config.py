# Configuration parameters for model and data paths
from dotenv import load_dotenv
load_dotenv()

MODEL_NAME = 'gpt2'  # Change to 'gpt-3.5-turbo' or HuggingFace model if needed
DATA_PATH = 'data/health_articles.csv'
TOP_K = 3
TEMPERATURE = 0.7
MAX_TOKENS = 100
