# StudyMate AI - Simple Study Chatbot
# Run: python StudyMate_push_to_talk_FULL.py

import tkinter as tk
from tkinter import scrolledtext
import webbrowser

UI = {"bg":"#0d1117","panel":"#0f1722","accent":"#3b82f6","text":"#e2e8f0","muted":"#94a3b8"}

# Databases (abbreviated for file size) - full coding DB included
MATH_DB = {
    "Calculus": {
        "Limits": {
            "keywords": ["limit", "limits", "continuity"],
            "description": "Limits & continuity — definitions, techniques, and examples.",
            "videos": ["https://youtu.be/Zc54gFhdpLA"],
            "pdfs": ["https://people.math.gatech.edu/~cain/notes/calculus.pdf"]
        },
        "Taylor Series": {
            "keywords": ["taylor", "maclaurin", "power series"],
            "description": "Taylor and Maclaurin series, radius of convergence and examples.",
            "videos": ["https://youtu.be/3d6DsjIBzJ4"],
            "pdfs": ["https://math.mit.edu/classes/18.01/notes/TaylorSeries.pdf"]
        }
    },
    "Linear Algebra": {
        "Matrices": {
            "keywords": ["matrix", "determinant", "eigen", "eigenvalue"],
            "description": "Matrices, determinants, eigenvalues and eigenvectors.",
            "videos": ["https://youtu.be/0gT2X7r0U3g"],
            "pdfs": ["https://math.mit.edu/~gs/linearalgebra/"]
        }
    }
}

PHYSICS_DB = {
    "Mechanics": {
        "Kinematics": {
            "keywords": ["kinematic", "kinematics", "velocity", "acceleration", "projectile"],
            "description": "1D & 2D motion, velocity, acceleration, projectile motion and examples.",
            "videos": ["https://youtu.be/hSjmIaj1fN0"],
            "pdfs": ["https://openstax.org/resources/colphys-2d-kinematics-pdf"]
        },
        "SHM": {
            "keywords": ["shm", "simple harmonic", "oscillation", "harmonic"],
            "description": "Simple Harmonic Motion: mass-spring, pendulum, and energy relations.",
            "videos": ["https://youtu.be/7K5p_q2uXgI"],
            "pdfs": ["https://openstax.org/resources/colphys-shm-pdf"]
        }
    },
    "Thermodynamics": {
        "Laws": {
            "keywords": ["thermodynamics", "entropy", "heat", "first law", "second law"],
            "description": "Basic thermodynamics: laws, energy, work, heat and entropy concepts.",
            "videos": ["https://youtu.be/3ngF7b0mK6k"],
            "pdfs": ["https://www.grc.nasa.gov/www/k-12/Numbers/Math/Math.html"]
        }
    }
}

CODING_DB = {
    "Python Basics": {
        "Variables": {
            "keywords": ["variable","datatype"],
            "description": "Variables store data.",
            "videos": ["https://youtu.be/kqtD5dpn9C8"],
            "pdfs": ["https://www.tutorialspoint.com/python/python_tutorial.pdf"]
        },
        "Data Types": {
            "keywords": ["int","float","string","list","dict"],
            "description": "Common Python data types.",
            "videos": ["https://youtu.be/D3JvDWO-BY4"],
            "pdfs": ["https://www.geeksforgeeks.org/python/python-data-types"]
        },
        "Operators": {
            "keywords": ["operators","arithmetic"],
            "description": "Operators in Python.",
            "videos": ["https://youtu.be/brMePLDi0-o?si=ORap1IKJ_dG_Woq6"],
            "pdfs": ["https://www.geeksforgeeks.org/python/python-operators"]
        }
    },
    "Flow Control": {
        "If-Else": {
            "keywords": ["if else","condition"],
            "description": "If-else statements.",
            "videos": ["https://youtu.be/f4KOjWS_KZs"],
            "pdfs": ["https://www.geeksforgeeks.org/python-if-else/"]
        },
        "Loops": {
            "keywords": ["for","while","loop"],
            "description": "For and while loops.",
            "videos": ["https://youtu.be/6iF8Xb7Z3wQ"],
            "pdfs": ["https://www.geeksforgeeks.org/python/loops-in-python"]
        }
    },
    "Functions": {
        "Functions": {
            "keywords": ["function","def"],
            "description": "Defining and using functions.",
            "videos": ["https://youtu.be/NSbOtYzIQI0"],
            "pdfs": ["https://www.geeksforgeeks.org/functions-in-python/"]
        },
        "Recursion": {
            "keywords": ["recursion","recursive"],
            "description": "Recursive functions.",
            "videos": ["https://youtu.be/Qk0zUZW-U_M"],
            "pdfs": ["https://www.geeksforgeeks.org/python/recursion-in-python"]
        },
        "Lambda": {
            "keywords": ["lambda","anonymous"],
            "description": "Lambda expressions.",
            "videos": ["https://youtu.be/25ovCm9jKfA"],
            "pdfs": ["https://www.geeksforgeeks.org/python-lambda-anonymous-functions/"]
        }
    },
    "OOP": {
        "Classes & Objects": {
            "keywords": ["class","object","oop"],
            "description": "Classes and objects in Python.",
            "videos": ["https://youtu.be/apACNr7DC_s"],
            "pdfs": ["https://www.programiz.com/python-programming/class"]
        },
        "Inheritance": {
            "keywords": ["inheritance"],
            "description": "Inheritance concept.",
            "videos": ["https://youtu.be/RSl87lqOXDE"],
            "pdfs": ["https://www.geeksforgeeks.org/python/inheritance-in-python"]
        }
    },
    "File Handling": {
        "File I/O": {
            "keywords": ["file","read","write"],
            "description": "Reading and writing files.",
            "videos": ["https://youtu.be/Uh2ebFW8OYM"],
            "pdfs": ["https://docs.python.org/3/tutorial/inputoutput.html"]
        }
    },
    "Exception Handling": {
        "Exceptions": {
            "keywords": ["exception","try","except"],
            "description": "Exception handling.",
            "videos": ["https://youtu.be/NIWwJbo-9_8"],
            "pdfs": ["https://docs.python.org/3/tutorial/errors.html"]
        }
    },
    "Data Structures": {
        "Lists": {"keywords":["list"],"description":"Lists."},
        "Dictionaries": {"keywords":["dict","dictionary"],"description":"Dictionaries."},
        "Sets": {"keywords":["set"],"description":"Sets."}
    },
    "DSA": {
        "Arrays": {"keywords":["array"],"description":"Arrays."},
        "Linked List": {"keywords":["linked list"],"description":"Linked lists."},
        "Stack": {"keywords":["stack"],"description":"Stacks."},
        "Queue": {"keywords":["queue"],"description":"Queues."},
        "Trees": {"keywords":["tree","bst"],"description":"Trees."},
        "Graphs": {"keywords":["graph"],"description":"Graphs."}
    },
    "Algorithms": {
        "Sorting": {"keywords":["sort","sorting"],"description":"Sorting algorithms."},
        "Searching": {"keywords":["search","binary","linear"],"description":"Searching algorithms."}
    }
}

DATABASES = {"math": MATH_DB, "physics": PHYSICS_DB, "coding": CODING_DB}

def find_response(text):
    q = text.lower().strip()
    if q in ("hello","hi","hey"):
        return {"text":"Hello 👋! What do you want to study? Try: Physics, Maths, Coding."}
    if "physics" in q:
        return {"text":"Physics selected ⚡ Try topics: kinematics, shm, thermodynamics."}
    if "math" in q:
        return {"text":"Math selected 📐 Try topics: limits, taylor series, matrices."}
    if "coding" in q or "python" in q:
        return {"text":"Coding selected 💻 Try topics: functions, loops, oop, dsa."}
    if any(k in q for k in ("resource","resources","links","notes","pdf","video")):
        return {"text":"Resources:\nhttps://bento.me/atc-first-year\nhttps://10cgpa.vercel.app\nhttps://92sgpa.vercel.app/"}
    for subj_db in DATABASES.values():
        for topics in subj_db.values():
            for tname, info in topics.items():
                if tname.lower() in q:
                    return info
                for kw in info.get("keywords", []):
                    if kw in q:
                        return info
    return {"text":"Sorry, I didn't understand. Try: 'physics kinematics', 'math taylor series', 'coding exceptions'."}

class StudyMateApp:
    def __init__(self, root):
        self.root = root
        root.title("StudyMate AI by ByteTalkers")
        root.geometry("900x650")
        root.configure(bg=UI["bg"])
        
        # Header
        header = tk.Frame(root, bg=UI["bg"], height=60)
        header.pack(fill="x", padx=10, pady=10)
        tk.Label(header, text="🧠 StudyMate AI", fg=UI["accent"], bg=UI["bg"], 
                font=("Segoe UI", 20, "bold")).pack(side="left", padx=10)
        tk.Label(header, text="by ByteTalkers", fg=UI["muted"], bg=UI["bg"], 
                font=("Segoe UI", 10)).pack(side="left")
        
        # Chat display
        self.chat = scrolledtext.ScrolledText(root, bg=UI["panel"], fg=UI["text"], 
                                              font=("Consolas", 11), wrap="word")
        self.chat.pack(fill="both", expand=True, padx=10, pady=(0,10))
        self.chat.config(state="disabled")
        self.chat.tag_config("link", foreground="#58a6ff", underline=True)
        self.chat.tag_bind("link", "<Button-1>", self.open_link)
        self.chat.tag_bind("link", "<Enter>", lambda e: self.chat.config(cursor="hand2"))
        self.chat.tag_bind("link", "<Leave>", lambda e: self.chat.config(cursor=""))
        
        # Quick buttons
        self.chips_frame = tk.Frame(root, bg=UI["bg"])
        self.chips_frame.pack(fill="x", padx=10, pady=(0,10))
        
        # Input area
        input_frame = tk.Frame(root, bg=UI["bg"])
        input_frame.pack(fill="x", padx=10, pady=(0,10))
        self.entry = tk.Entry(input_frame, bg=UI["panel"], fg=UI["text"], 
                             font=("Segoe UI", 12), insertbackground=UI["text"])
        self.entry.pack(side="left", fill="x", expand=True, padx=(0,8), ipady=8)
        self.entry.bind("<Return>", lambda e: self.on_send())
        tk.Button(input_frame, text="Send ➤", bg=UI["accent"], fg="white", 
                 relief="flat", command=self.on_send, padx=20).pack(side="right")
        
        self.insert_bot("Hello! 👋 Ask me about Physics, Math, or Coding.")
        self.update_chips_default()

    def insert_user(self, text):
        self.chat.config(state="normal")
        self.chat.insert("end", f"\nYou: {text}\n")
        self.chat.config(state="disabled")
        self.chat.yview("end")

    def insert_bot(self, text):
        self.chat.config(state="normal")
        self.chat.insert("end", f"\nStudyMate: ")
        self.insert_text_with_links(text)
        self.chat.insert("end", "\n")
        self.chat.config(state="disabled")
        self.chat.yview("end")

    def insert_text_with_links(self, text):
        # Split by both spaces and newlines to properly handle all tokens
        lines = text.split('\n')
        for i, line in enumerate(lines):
            tokens = line.split()
            for t in tokens:
                if t.startswith("http://") or t.startswith("https://"):
                    self.chat.insert("end", t + " ", "link")
                else:
                    self.chat.insert("end", t + " ")
            # Add newline after each line except the last
            if i < len(lines) - 1:
                self.chat.insert("end", "\n")
                
    def open_link(self, event):
        idx = self.chat.index(f"@{event.x},{event.y}")
        try:
            start = self.chat.index(f"{idx} wordstart")
            end = self.chat.index(f"{idx} wordend")
            url = self.chat.get(start, end).strip()
            if url.startswith("http"):
                webbrowser.open(url)
        except Exception:
            pass

    def clear_chips(self):
        for w in self.chips_frame.winfo_children():
            w.destroy()

    def add_chip(self, label, command=None):
        b = tk.Button(self.chips_frame, text=label, bg="#111827", fg=UI["text"], relief="flat",
                      padx=10, pady=6, command=command or (lambda l=label: self.on_chip_click(l)))
        b.pack(side="left", padx=6, pady=6)

    def update_chips_for_subject(self, subject_key):
        self.clear_chips()
        db = DATABASES.get(subject_key, {})
        for category, topics in db.items():
            for topic_name in topics.keys():
                self.add_chip(topic_name, lambda t=topic_name: self.send_text_and_respond(t))
        self.add_chip("resources", lambda: self.send_text_and_respond("resources"))

    def update_chips_default(self):
        self.clear_chips()
        defaults = ["hello", "physics", "math", "coding", "resources"]
        for d in defaults:
            self.add_chip(d, lambda dd=d: self.send_text_and_respond(dd))

    def on_chip_click(self, label):
        self.send_text_and_respond(label)

    def on_send(self):
        text = self.entry.get().strip()
        if not text:
            return
        self.entry.delete(0, "end")
        self.insert_user(text)
        self.handle_query(text)

    def send_text_and_respond(self, text):
        self.insert_user(text)
        self.handle_query(text)

    def handle_query(self, text):
        lowered = text.lower()
        if "physics" in lowered:
            self.update_chips_for_subject("physics")
        elif "math" in lowered or "mathematics" in lowered:
            self.update_chips_for_subject("math")
        elif "coding" in lowered or "python" in lowered:
            self.update_chips_for_subject("coding")
        res = find_response(text)
        if "description" in res:
            msg = res.get("description", "")
            vids = res.get("videos", [])
            pdfs = res.get("pdfs", [])
            if vids:
                msg += "\n\n🎥 Videos:\n" + "\n".join(vids)
            if pdfs:
                msg += "\n\n📄 PDFs:\n" + "\n".join(pdfs)
            self.insert_bot(msg)
        else:
            self.insert_bot(res.get("text", "Sorry, I couldn't find info."))

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyMateApp(root)
    root.mainloop()
