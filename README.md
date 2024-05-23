# LLM-Retail-Solution-Langchain-Google-Palm-Integration-for-Retail-Industry

This is an end-to-end LLM project based on Google Palm and Langchain. We are building a system that can talk to a MySQL database. User asks questions in natural language, and the system generates answers by converting those questions to an SQL query and then executing that query on a MySQL database. zeho Tees is a T-shirt store where they maintain their inventory, sales, and discounts data in a MySQL database. A store manager may ask questions such as,

- How many white color Adidas t-shirts do we have left in the stock?
- How much sales will our store generate if we can sell all extra-small size t-shirts after applying discounts?

The system is intelligent enough to generate accurate queries for given questions and execute them on the MySQL database.

## Project Highlights

- zeho Tees is a t-shirt store that sells Adidas, Nike, Van Heusen, and Levi's t-shirts.
- Their inventory, sales, and discounts data are stored in a MySQL database.
- We will build an LLM-based question and answer system that will use the following:
  - Google Palm LLM
  - Google Generative AI Embeddings
  - Streamlit for UI
  - Langchain framework
  - Chroma DB for vector store
  - Few-shot learning

In the UI, the store manager will ask questions in natural language, and it will produce the answers.

## Installation

1. Clone this repository to your local machine using:

   ```bash
   gh repo clone zehowrld/LLM-Retail-Solution-Langchain-Google-Palm-Integration-for-Retail-Industry
   ```

2. Navigate to the project directory:

   ```bash
   cd LLM-Retail-Solution-Langchain-Google-Palm-Integration-for-Retail-Industry
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Acquire an API key through makersuite.google.com and put it in the `.env` file:

   ```bash
   GOOGLE_API_KEY="your_api_key_here"
   ```

5. For database setup, run `database/db_creation_zeho_t_shirts.sql` in your MySQL workbench.

## Usage

1. Run the Streamlit app by executing:

   ```bash
   streamlit run app.py
   ```

2. The web app will open in your browser where you can ask questions.

## Sample Questions

- How many total t-shirts are left in stock?
- How many t-shirts do we have left for Nike in XS size and white color?
- How much is the total price of the inventory for all S-size t-shirts?
- How much sales amount will be generated if we sell all small size Adidas shirts today after discounts?

## Project Structure

- `app.py`: The main Streamlit application script.
- `langchain_helper.py`: This has all the Langchain code.
- `requirements.txt`: A list of required Python packages for the project.
- `few_shots.py`: Contains few-shot prompts.
- `.env`: Configuration file for storing your Google API key.
```
