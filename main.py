import openai
import dotenv 

# secrets for API keys
env_path = os.path.join(os.path.dirname(__file__), '..', 'secrets', '.env')
load_dotenv(env_path)

OPENAI_KEY = os.getenv("OPENAI_API_KEY")


