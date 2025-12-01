1.) Create a Conda or normal Virtual Environment

2.) Install all the required package using the below command 
   > pip install -r requirement.txt

3.) Create a .env file and paste your google_api_key (get in the google AI studio)
    GOOGLE_API_KEY = "YOUR KEY"

4.) If you want to create the new table in the student.db first execute the sqlite.py with your prefered table name and values (Table name must be upper_case).

5.) If ok to use the pre-stoed value just run the sql.py using streamlit
  > streamlit run app.py
