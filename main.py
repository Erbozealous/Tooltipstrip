# tooltipstrip.py
# Version 0.1
# Designed to convert weapon tooltips from links to the new InfoBoxes
# Made this with AI in around 20 minutes lol
# Erbozealous

# HOW TO USE:
# Download the file
# Run the file with `python tooltipstrip.py`
# Paste your text into the input box
# Click "Convert"
# Click "Clear" to clear both input and output boxes

# NOTE: Cannot differentiate between lasers and sustained beams. You're gonna have to do that manually 
# Will default to laser tooltip if not specified

'''
Example input:

| spinals = 1x [[Rebel Quad Heavy Ion Cannon]]
| missiles = 8x [[Concussion Missile]]
| lasers = 6x [[Rebel Small Cannon Hybrid]]
<li> 6x [[Rebel Large Turbolaser]]
<li> 6x [[Rebel Medium Turbolaser]]
<li> 8x [[Rebel Medium Ion Cannon]]
<li> 6x [[Rebel Heavy Ion Cannon]]


Example output:

| spinals = 1x {{Tooltip|Rebel Quad Heavy Ion Cannon|{{LaserInfobox|Rebel Quad Heavy Ion Cannon}}}}
| missiles = 8x {{Tooltip|Concussion Missile|{{MissileInfobox|Concussion Missile}}}}
| lasers = 6x {{Tooltip|Rebel Small Cannon Hybrid|{{LaserInfobox|Rebel Small Cannon Hybrid}}}}
<li> 6x {{Tooltip|Rebel Large Turbolaser|{{LaserInfobox|Rebel Large Turbolaser}}}}
<li> 6x {{Tooltip|Rebel Medium Turbolaser|{{LaserInfobox|Rebel Medium Turbolaser}}}}
<li> 8x {{Tooltip|Rebel Medium Ion Cannon|{{LaserInfobox|Rebel Medium Ion Cannon}}}}
<li> 6x {{Tooltip|Rebel Heavy Ion Cannon|{{LaserInfobox|Rebel Heavy Ion Cannon}}}}
'''




import tkinter as tk
from tkinter import ttk
import re

class TooltipConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Erb's Awesome Weapon Tooltip Converter")
        self.root.geometry("800x600")
        
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create and configure text areas
        self.input_text = tk.Text(main_frame, height=12, width=80)
        self.input_text.grid(row=0, column=0, pady=5)
        self.input_text.insert('1.0', "")
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=0, pady=5)
        
        # Convert button
        convert_button = ttk.Button(button_frame, text="Convert", command=self.convert_text)
        convert_button.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        clear_button = ttk.Button(button_frame, text="Clear", command=self.clear_text)
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Output text area
        self.output_text = tk.Text(main_frame, height=12, width=80)
        self.output_text.grid(row=2, column=0, pady=5)
        
        # Bind double-click to select all text
        self.input_text.bind('<Double-Button-1>', lambda e: self.select_all(self.input_text))
        self.output_text.bind('<Double-Button-1>', lambda e: self.select_all(self.output_text))
        
        # Make window resizable
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
    
    def select_all(self, widget):
        widget.tag_add(tk.SEL, "1.0", tk.END)
        widget.mark_set(tk.INSERT, "1.0")
        widget.see(tk.INSERT)
        return 'break'
    




    

    def convert_text(self):
        # Newline handling
        input_text = self.input_text.get('1.0', 'end-1c')  # end-1c removes the extra newline
        

        # NOTE: Cannot differentiate between lasers and sustained beams. You're gonna have to do that manually 
        # Will default to laser tooltip if not specified
        # Actually will just do laser I haven't added sustained beams at all
        # Oh and missiles too

        # Reaper L

        category = [0]  # use a list to make it mutable from inner function

        def make_replacer(category):
            def replace_weapon(match):
                weapon_name = match.group(1)
                line = match.string[:match.start()].splitlines()[-1] if match.string[:match.start()].splitlines() else ""
                line_lower = line.lower()


                if re.search(r'\|.*', weapon_name): weapon_name = re.sub(r'\|.*', '', weapon_name)  # Remove any leading pipe characters


                if "laser" in line_lower:
                    category[0] = 1
                    return f"{{{{Tooltip|{weapon_name}|{{{{LaserInfobox|{weapon_name}}}}}}}}}"
                elif "missile" in line_lower:
                    category[0] = 2
                    return f"{{{{Tooltip|{weapon_name}|{{{{MissileInfobox|{weapon_name}}}}}}}}}"
                elif "pointdefense" in line_lower or "point defense" in line_lower:
                    category[0] = 3
                    return f"{{{{Tooltip|{weapon_name}|{{{{PointDefenseInfobox|{weapon_name}}}}}}}}}"
                else: # If no category is found, use the last known category
                    if category[0] == 1:
                        return f"{{{{Tooltip|{weapon_name}|{{{{LaserInfobox|{weapon_name}}}}}}}}}"
                    elif category[0] == 2:
                        return f"{{{{Tooltip|{weapon_name}|{{{{MissileInfobox|{weapon_name}}}}}}}}}"
                    elif category[0] == 3:
                        return f"{{{{Tooltip|{weapon_name}|{{{{PointDefenseInfobox|{weapon_name}}}}}}}}}"
                    else:
                        return f"{{{{Tooltip|{weapon_name}|{{{{LaserInfobox|{weapon_name}}}}}}}}}"
            return replace_weapon

        
        # Convert the text using regex
        converted_text = re.sub(r'\[\[(.*?)\]\]', make_replacer(category), input_text)
        
        # Strip any trailing newlines and only add back if input had one
        converted_text = converted_text.rstrip()
        
        # Update output text
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert('1.0', converted_text)
    
    def clear_text(self):
        self.input_text.delete('1.0', tk.END)
        self.output_text.delete('1.0', tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TooltipConverter()
    app.run()




