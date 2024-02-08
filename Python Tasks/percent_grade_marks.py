obtained_marks=int(input("Enter obtained mrks: "))
perecent=float(obtained_marks/150)*100
# p="Perecent"
if perecent>=120:
    print(perecent,"percentage  A Grade")
elif perecent>90 and perecent<120:
    print("B Grade",perecent,p)
elif perecent>60 and perecent<90:
    print("C Grade",perecent,p)
else:
    print("Fail")