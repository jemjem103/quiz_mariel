import tkinter as tk
from tkinter import messagebox
from tkinter import *

class MarielPythonQuiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mariel Quiz Game fun fact about BSIS_SUSE ")
        self.resizable(False, False)
        self.geometry("900x600")
        self.configure(bg="#DDA0DD")

        bg = PhotoImage(file = "BSIS_SUSE.png")

        canvas1 = Canvas(self, width = 400, height = 200)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(0,0, image=bg, anchor="nw")
        self.bg = bg
        

        self.questions = [
            ("Q1 What is the first and last lesson of sir Robert Salonga? \nHint: Al_ori_hm", "Algorithm"),
            ("Q2 Sino ang pinaka poging sigbin sa BSIS-SUSE?\nHint: K_e_l_y", "Khelly"),
            ("Q3 Pinaka magandang President ng SUSE?\nHint: Mar_el", "Mariel"),
            ("Q4 Apelido ng handsome major subject ng BSIS-SUSE?\nHint: _alo_a", "Salonga"),
            ("Q5 Mahilig mag BJ kaya na la-late (BJ-BukoJuice)?\nHint: Jh_d_l", "Jhodel"),
            ("Q6 Pinaka maraming Nursing kaya sabi ni Khelly Malandi sya?\nHint: _nge_o", "Angelo"),
            ("Q7 Babae sya kaya palagi syang tama?\nHint: E_yza", "Elyza"),
            ("Q8 Wala na sya ngayon pero andito kaapelido nya?\nHint: M_nieg_", "Maniego"),
            ("Q9 Sa buong Course ng BSIS sila ang pinaka masasarap?\nHint: S_S_", "SUSE"),
        ]

        self.existing_question = 0
        self.question_label = tk.Label(self, text="", bg="#DDA0DD", fg="#800000", font=("Bodoni MT", 22))
        
        self.question_label.pack(pady=30)

        self.answer_entry = tk.Entry(self, font=("Serif", 25))
        self.answer_entry.pack(pady=20)

        self.submit_button = tk.Button(self, text="Ipasok mo na beybe", command=self.Validate_Response)
        self.submit_button.pack(pady=20)

        self.Initialize_Question()

    def Initialize_Question(self):
        if self.existing_question < len(self.questions):
            throwable_value, _ = self.questions[self.existing_question]
            self.question_label.config(text=throwable_value)
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Last Questionaire", "NADALI MO IDOL!!\nIT MEANS...\nYou have completed the quiz!")
            self.destroy()

    def Validate_Response(self):
        User_Response = self.answer_entry.get()
        _, correct_answer = self.questions[self.existing_question]

        if User_Response.lower() == correct_answer.lower():
            messagebox.showinfo("Unquestionable", "Your reaction   （づ￣3￣）づ╭❤️～,\nresponse ✧o❤o✧o❤o✧o❤o \neven reply is not LEFT but RIGHT so it's exactly valid MAGALING KA AH ALAM MO AHH!!!")
        else:
            messagebox.showerror(
                "Erroneous", f"Pardon me, medyo tagilid tayo dyan\n Tao nare ayusin mo naman!!\n Para tumama ka o tatamaan ka?\n the authentic valid and legitimate result is {correct_answer}."  
            )

        self.existing_question += 1
        self.Initialize_Question()


if __name__ == "__main__":
    app = MarielPythonQuiz()
    app.mainloop()
