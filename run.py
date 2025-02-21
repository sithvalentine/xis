# run.py
import subprocess
import os


def run_streamlit():
    try:
        # Get the current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Activate virtual environment and run streamlit
        subprocess.run([
            'source venv/bin/activate && streamlit run app.py',
        ], shell=True, cwd=current_dir)

    except Exception as e:
        print(f"Error running Streamlit: {e}")


if __name__ == "__main__":
    run_streamlit()