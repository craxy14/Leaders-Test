def directions(walk):
    if len(walk) == 10:
        if "n" in walk and "s" in walk and "w" in walk and "e" in walk:
            return walk.count("n") == walk.count("s")
        elif "n" in walk and "s" in walk and "w" in walk:
            return walk.count("n") == walk.count("s")
        elif "n" in walk and "s" in walk:
            return walk.count("n") == walk.count("s")
        elif "n" in walk and "w" in walk:
            return walk.count("n") == walk.count("w")
        elif "n" in walk and "e" in walk:
            return walk.count("n") == walk.count("e")
        elif "s" in walk and "w" in walk:
            return walk.count("s") == walk.count("w")
        elif "s" in walk and "e" in walk:
            return walk.count("s") == walk.count("e")
        elif "w" in walk and "n" in walk:
            return walk.count("w") == walk.count("n")
        elif "w" in walk and "s" in walk:
            return walk.count("w") == walk.count("s")
        elif "w" in walk and "e" in walk:
            return walk.count("w") == walk.count("e")
        
    return False

print(directions(['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w']))