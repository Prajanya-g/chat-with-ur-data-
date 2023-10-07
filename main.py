import sqlite3
import pandas as pd
import connectLocalSQL as createSQL
import os
from credentials import openAIKey
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
import tkinter as tk
import tkinter.ttk as ttk

db_file = 'sample.db'
sql_file = 'sampleDatabase.sql'

# Check if the database file already exists
if not os.path.exists(db_file):
    # Create the SQLite database if it doesn't exist
    createSQL.create_sqlite_database(db_file, sql_file)
else:
    print(f"The database file '{db_file}' already exists. Skipping creation.")

# Fetch the OpenAI key
os.environ['OPENAI_API_KEY'] = openAIKey

db = SQLDatabase.from_uri("sqlite:///./sample.db")
llm = OpenAI()
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True
)

# Create the button callback
def on_click():
    # Get the query text from the entry widget
    query = entry.get()

    # Disable the entry widget while processing
    entry.config(state="disabled")

    # Run the query using the agent executor
    result = agent_executor.run(query)

    # Display the result in the text widget
    text.delete("1.0", tk.END)
    text.insert(tk.END, result)

    # Clear the entry field after the query is complete
    entry.delete(0, tk.END)

    # Re-enable the entry widget
    entry.config(state="normal")

# Create the UI window
root = tk.Tk()
root.title("Chat with your Data")

# Add a label for the entry widget
label = ttk.Label(root, text="Enter your question:", font=("Arial", 14))
label.pack(padx=20, pady=10)

# Create the text entry widget
entry = ttk.Entry(root, font=("Arial", 14))
entry.pack(padx=20, pady=5, fill=tk.X)

# Set the focus on the text entry widget
entry.focus()

# Create the button widget
button = ttk.Button(root, text="Chat", command=on_click)
button.pack(padx=20, pady=10)

# Bind Enter key press event to the "Chat" button
root.bind('<Return>', lambda event=None: button.invoke())

# Create a frame for the text widget and add scrollbars
text_frame = tk.Frame(root)
text_frame.pack(padx=20, pady=10)
text_scrollbar_y = ttk.Scrollbar(text_frame, orient=tk.VERTICAL)
text_scrollbar_x = ttk.Scrollbar(text_frame, orient=tk.HORIZONTAL)
text = tk.Text(text_frame, height=10, width=60, font=("Arial", 14),
              yscrollcommand=text_scrollbar_y.set, xscrollcommand=text_scrollbar_x.set)
text.pack(fill=tk.BOTH)
text_scrollbar_y.config(command=text.yview)
text_scrollbar_x.config(command=text.xview)
text_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
text_scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

# Start the UI event loop
root.mainloop()
