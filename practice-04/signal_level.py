signal_intensity = int(input())

if signal_intensity < 20:
    print("Потрібна увага: Слабкий сигнал")
    
elif signal_intensity in range(20, 60):
    print("Звичайний режим: Робочий діапазон")
elif signal_intensity in range (61, 96):
        print(" Звичаний режим: Сильний сигнал")
else:
    print("Потрібна увага: насичення фотоприймача")
