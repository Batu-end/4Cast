import os

def main():
    streamlit_path = "app.py"

    os.system(f'streamlit run {streamlit_path}')

if __name__ == "__main__":
    main()