from dotenv import load_dotenv
load_dotenv()
import pandas as pd

df = pd.read_csv('examples/trace_results.csv')

accuracy = df['grounded'].sum() / len(df)
print(f"Grounded QA Accuracy: {accuracy:.2f}")

# Show problematic samples
print("\nUngrounded Responses:")
print(df[df['grounded'] == False][['query', 'generated_answer', 'notes']])
