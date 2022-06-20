print("POKEMON CALCULATOR\n1. Stats\n2. EV")
import EV, STATS, main

opt_1 = 0

opt = int(input("-->"))

stats_core = ["HP","Attack","Defense","Special Attack","Special Defense","Speed"]

def values():
    global stat_inp, arr, base, IV, EV, lvl, natures
    base, stat_inp = 0, 0
    arr = []
    if opt_1 == 2:
        print("BASE:")
        for a in range (len(stats_core)):
            inp = int(input(stats_core[a]))
            arr.append(inp)     
    else:   
        for b in range (len(stats_core)):
            print(b+1,".",stats_core[b])
        stat_inp = int(input("-->"))   
        print("\n",stats_core[stat_inp-1].upper())   
        base = int(input("Base: "))
    IV = int(input("IV (1-31): "))
    EV = int(input("EV (1-255): "))
    lvl = int(input("Level: "))

    if stat_inp > 1 or stats_core[stat_inp-1] != "HP":
        print("What Nature?")
        print("\t1. Hardy       6. Bold        11. Timid       16. Modest       21. Calm")
        print("\t2. Lonely      7. Docile      12. Hasty       17. Mild         22. Gentle")
        print("\t3. Brave       8. Relaxed     13. Serious     18. Quiet        23. Sassy")
        print("\t4. Adamant     9. Impish      14. Jolly       19. Bashful      24. Careful")
        print("\t5. Naughty     10. Lax        15. Naive       20. Rash         25. Quirky")
        natures = int(input("Nature: "))
    else: natures = 0

def error1(): 
    print("Invalid Input")
    out()

def out():
    input("Press enter to continue...")
    main

if opt == 1:
    print("\nPOKEMON STATS CALCULATOR")
    values()
    print(stats_core[stat_inp-1],"-->", STATS.userstat.stat(stat_inp,base,IV,EV,lvl,natures), end="\n\n")
    out()
    
elif opt == 2:
    del stats_core[0]
    print("\nEV CALCULATOR\n1. Single Stat\n2. All Stats")
    opt_1 = int(input("-->"))
    if(opt_1 == 1):
        print("\nSINGLE STAT")
        values()
        stat = int(input("Desire Stat: "))
        print("EV Needed on",stats_core[stat_inp-1].upper(),"-->", EV.userev.single(stat_inp,base,IV,EV,lvl,natures,stat), end="\n\n")
    elif(opt_1 == 2): 
        print("\nALL STAT")
        stats_core = [stats_core + "-->" for stats_core in stats_core]  
        values()
        desire = []
        print("\nDesire Stats:")
        for b in range (len(stats_core)):
            stat = int(input(stats_core[b]))
            desire.append(stat)
        print("\nEVs Needed on:")
        for c in range (len(stats_core)):
            print(stats_core[c],EV.userev.all(desire,arr[c],desire[c],IV,EV,lvl,natures,stat), end="\n")
        print("\n")
    else: error1()
    out()

else: error1()

