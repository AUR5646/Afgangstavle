from tkinter import*


class DepartureBoardView:
   
    def __init__(self):            
        self.root = Tk()
        self.root.geometry("800x300")
        self.root.title("Rejseplanen tavle") 
        icon = PhotoImage(file="rs.png")
        self.root.iconphoto(True, icon)

        L1 = Label(self.root, text="København Syd, Grøntorvet",
        anchor="w", font=("normal", 14,"bold"))
        L1.grid(row=0, column=0, columnspan=2)

        header1 = Label(self.root, text="Bus", width=10,
        anchor="w", font=("normal", 13, "bold"))
        
        header1.grid(row=1, column=0, padx=5, pady=5)

        header2 = Label(self.root, text="Destination", width=20,
        anchor="w", font=("normal", 13, "bold"))
        header2.grid(row=1, column=1, padx=5, pady=5)

        header3 = Label(self.root, text="Planmæssig\nafgang", width=10,
        anchor="w",justify="left", font=("normal", 13,"bold"))
        header3.grid(row=1, column=2, padx=5, pady=5)

        header4 = Label(self.root, text="forventet\nafgang", width=10,
        anchor="w",justify="left", font=("normal", 13,"bold"))
        header4.grid(row=1, column=3, padx=5, pady=5)

        header5 = Label(self.root, text="Ankommer\nom", width=10,
        anchor="w",justify="left", font=("normal", 13,"bold"))
        header5.grid(row=1, column=4, padx=5, pady=5)

        self.refresh_button = Button(self.root, text="↪️",
                                     font=("Arial", 20), command=self.refresh)
        self.refresh_button.grid(row=3, column=6)

        
    def display(self, departures):
        j = 2
        for i in departures:
            Label(self.root, text=i.get("name"), width=10, anchor="w"
                 ).grid(row=j, column=0, padx=5, pady=2)

            Label(self.root, text=i.get("direction"), width=20, anchor="w"
                 ).grid(row=j, column=1, padx=5, pady=2)

            Label(self.root, text=i.get("scheduled"), width=10, anchor="w"
                 ).grid(row=j, column=2, padx=5, pady=2)

            Label(self.root, text=i.get("actual"), width=10, anchor="w"
                 ).grid(row=j, column=3, padx=5, pady=2)

            Label(self.root, text=i.get("within"), width=10, anchor="w"
                 ).grid(row=j, column=4, padx=5, pady=2)
            j += 1

    def refresh(self):
        print("Refresh button pressed")


     





