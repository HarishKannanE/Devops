# Keywords arguments
def vac_feedback(vac, efficacy):
    print(f"{vac} Vaccine is having {efficacy}% efficacy.")
    if (efficacy > 50) and (efficacy <= 75):
        print("Seems not so effactive, needs more trial.")
    elif (efficacy > 75) and (efficacy < 90):
        print("Can consider this vaccine.")
    elif efficacy >= 90:
        print("Sure, will take the shot.")
    else:
        print("Needs many more trials.")

# vac_feedback("pfizer", 95)
# vac_feedback(20, "unknown")
vac_feedback(efficacy=30, vac="covaxin")