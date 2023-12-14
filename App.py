import customtkinter as ctk
from tkinter import PhotoImage
from PIL import ImageTk, Image



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Simulation Interface")
        self.geometry("900x600")
        self.minsize(900, 600)
        self.maxsize(900, 600)
        self.resizable(False, False)
        image = Image.open("assets/Logos.png")
        self.logo = ImageTk.PhotoImage(image)
        self.start_page = StartPage(self)
        self.menu_page = None
        self.perception_page = None
        self.mainloop()

class StartPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.create_widgets()
    
    def create_widgets(self):
        self.canvas = ctk.CTkCanvas(self, bg="#171717", height=600, width=900, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0.0, 0.0, 360.0, 600.0, fill="#D9D9D9", outline="")
        
        self.canvas.create_image(180.0, 80.0, anchor="center", image=self.master.logo)

        self.canvas.create_text(15.0, 150.0, anchor="nw", text="Formula Students AI", fill="#DA0037", font=("Ubuntu", 32 * -1))
        self.canvas.create_text(15.0, 200.0, anchor="nw", text="Simulation\nInterface", fill="#000000", font=("Ubuntu", 64 * -1))
        self.canvas.create_text(15.0, 355.0, anchor="nw", text="Welcome to FSAI’s Simulation \nInterface. To start please\nchoose a simulator.", fill="#444444", font=("Ubuntu", 24 * -1))

        self.canvas.create_text(405.0,50, anchor="nw", text="Choose a simulator: ", fill="#EDEDED", font=("Ubuntu", 32 * -1))
        self.button_1 = ctk.CTkButton(self, width=455, height=75,text="CARLA", bg_color="#171717", fg_color="#DA0037", command=lambda: self.open_module_page("CARLA"), font=("Ubuntu", 32 * -1))
        self.button_1.place(x=405.0, y=100.0)

        self.button_2 = ctk.CTkButton(self, width=455, height=75,text="CarMaker", bg_color="#171717", fg_color="#DA0037", command=lambda: self.open_module_page("CarMaker"), font=("Ubuntu", 32 * -1))
        self.button_2.place(x=405.0, y=200.0)



        

    def open_module_page(self, simulator):
        self.master.start_page.pack_forget()
        self.master.menu_page = MenuPage(self.master, simulator)
        self.master.menu_page.pack()

class MenuPage(ctk.CTkFrame):
    def __init__(self, master, simulator):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.simulator = simulator
        self.create_widgets(self.simulator)
    
    def create_widgets(self, simulator):
        self.canvas = ctk.CTkCanvas(self, bg="#171717", height=600, width=900, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0.0, 0.0, 360.0, 600.0, fill="#D9D9D9", outline="")

        self.canvas.create_image(180.0, 80.0, anchor="center", image=self.master.logo)

        self.canvas.create_text(15.0, 150.0, anchor="nw", text="Formula Students AI", fill="#DA0037", font=("Ubuntu", 32 * -1))
        self.canvas.create_text(15.0, 200.0, anchor="nw", text="Simulation\nInterface", fill="#000000", font=("Ubuntu", 64 * -1))
        self.canvas.create_text(15.0, 360.0, anchor="nw", text=simulator, fill="#444444", font=("Ubuntu", 32 * -1))

        self.canvas.create_text(405.0,50, anchor="nw", text="Choose a module: ", fill="#EDEDED", font=("Ubuntu", 32 * -1))
        self.button_1 = ctk.CTkButton(self, width=455, height=75,text="Perception", bg_color="#171717", fg_color="#DA0037", command=lambda: self.open_module_page("Perception"), font=("Ubuntu", 32 * -1))
        self.button_1.place(x=405.0, y=100.0)
        self.button_2 = ctk.CTkButton(self, width=455, height=75,text="Planning", bg_color="#171717", fg_color="#DA0037", command=lambda: self.open_module_page("Planning"), font=("Ubuntu", 32 * -1))
        self.button_2.place(x=405.0, y=200.0)
        self.button_3 = ctk.CTkButton(self, width=455, height=75,text="Control", bg_color="#171717", fg_color="#DA0037", command=lambda: self.open_module_page("Control"), font=("Ubuntu", 32 * -1))
        self.button_3.place(x=405.0, y=300.0)
        self.button_4 = ctk.CTkButton(self, width=455, height=75,text="SLAM", bg_color="#171717", fg_color="#DA0037", command=lambda: self.open_module_page("Simulation"), font=("Ubuntu", 32 * -1))
        self.button_4.place(x=405.0, y=400.0)
        self.button_5 = ctk.CTkButton(self, width=330, height=75,text="Back", bg_color="#D9D9D9", fg_color="#DA0037", command=lambda: self.open_start_page(), font=("Ubuntu", 32 * -1))
        self.button_5.place(x=15.0, y=500.0)

    def open_start_page(self):
        self.master.start_page.pack(fill="both", expand=True)
        self.pack_forget()

    def open_module_page(self, module):
        self.master.start_page.pack_forget()
        self.pack_forget()
        if module == "Perception":
            module_page = PerceptionPage(self.master, self.simulator)
        elif module == "Planning":
            module_page = PlanningPage(self.master, self.simulator)
        elif module == "Control":
            module_page = ControlPage(self.master, self.simulator)
        elif module == "Simulation":
            module_page = SimulationPage(self.master, self.simulator)
        module_page.pack()

class ControlPage(ctk.CTkFrame):
    def __init__(self, master, simulator):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.simulator = simulator
        self.create_widgets(self.simulator)

    def create_widgets(self, simulator):
        self.canvas = ctk.CTkCanvas(self, bg="#171717", height=600, width=900, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0.0, 0.0, 360.0, 600.0, fill="#D9D9D9", outline="")
        self.canvas.create_image(180.0, 80.0, anchor="center", image=self.master.logo)
        self.canvas.create_text(15.0, 150.0, anchor="nw", text="Formula Students AI", fill="#DA0037", font=("Ubuntu", 32 * -1))
        self.canvas.create_text(15.0, 200.0, anchor="nw", text="Simulation\nInterface", fill="#000000", font=("Ubuntu", 64 * -1))
        self.canvas.create_text(15.0, 360.0, anchor="nw", text=simulator, fill="#444444", font=("Ubuntu", 32 * -1))
        self.canvas.create_text(15.0, 410.0, anchor="nw", text="Control", fill="#444444", font=("Ubuntu", 32 * -1))

        self.canvas.create_text(405.0,50, anchor="nw", text="Write your topic names: ", fill="#EDEDED", font=("Ubuntu", 32 * -1))
        self.canvas.create_text(405.0,100, anchor="nw", text="Inputs", fill="#DA0037", font=("Ubuntu", 28 * -1))
        self.canvas.create_text(405.0,140, anchor="nw", text="Odometry (Odometry):", fill="#EDEDED", font=("Ubuntu", 22 * -1))
        self.odometry_entry = ctk.CTkEntry(self, width=455, height=25, bg_color="#171717", fg_color="#EDEDED", font=("Ubuntu", 22 * -1))
        self.odometry_entry.place(x=405.0, y=170.0)
        self.canvas.create_text(405.0,210, anchor="nw", text="Waypoints (Path):", fill="#EDEDED", font=("Ubuntu", 22 * -1))
        self.waypoints_entry = ctk.CTkEntry(self, width=455, height=25, bg_color="#171717", fg_color="#EDEDED", font=("Ubuntu", 22 * -1))
        self.waypoints_entry.place(x=405.0, y=240.0)
        self.canvas.create_text(405.0,300, anchor="nw", text="Outputs", fill="#DA0037", font=("Ubuntu", 28 * -1))
        self.canvas.create_text(405.0,330, anchor="nw", text="Control Actions (AckermannDrive):", fill="#EDEDED", font=("Ubuntu", 22 * -1))
        self.control_actions_entry = ctk.CTkEntry(self, width=455, height=25, bg_color="#171717", fg_color="#EDEDED", font=("Ubuntu", 22 * -1))
        self.control_actions_entry.place(x=405.0, y=360.0)

        self.button_1 = ctk.CTkButton(self, width=330, height=75,text="Back", bg_color="#D9D9D9", fg_color="#DA0037", command=lambda: self.open_menu_page(), font=("Ubuntu", 32 * -1))
        self.button_1.place(x=15.0, y=500.0)
        self.button_2 = ctk.CTkButton(self, width=330, height=75,text="Start", bg_color="#171717", fg_color="#DA0037", command=lambda: self.start_simulation(), font=("Ubuntu", 32 * -1))
        self.button_2.place(x=465.0, y=500.0)

        #start simulation on enter
        self.odometry_entry.bind("<Return>", lambda event: self.start_simulation())
        self.waypoints_entry.bind("<Return>", lambda event: self.start_simulation())
        self.control_actions_entry.bind("<Return>", lambda event: self.start_simulation())

    def open_menu_page(self):
        self.master.menu_page.pack(fill="both", expand=True)
        self.pack_forget()

    def start_simulation(self):
        odometry = self.odometry_entry.get()
        waypoints = self.waypoints_entry.get()
        control_actions = self.control_actions_entry.get()
        if odometry == "" or waypoints == "" or control_actions == "":
            self.canvas.create_text(405.0, 450.0, anchor="nw", text="Please fill in all the fields", fill="#DA0037", font=("Ubuntu", 24 * -1))
        else:
            # TODO: Start simulation
            print("----- Simulation Started -----")
            print("Odometry Topic: " + odometry)
            print("Waypoints Topic: " + waypoints)
            print("Control Actions Topic: " + control_actions)


if __name__ == "__main__":
    App()
