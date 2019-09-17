def speed_penality(speed):
    if speed <= 50:
        return "ok" 
    elif speed <= 55:
        return "€10"
    elif speed <= 60:
        return "€20"
    elif speed <= 65:
        return "€30"
    elif speed <= 70:
        return "€40"
    elif speed <= 75:
        return "€50"
    elif speed <= 80:
        return "€60"
    else:
        return "license taken"


    
