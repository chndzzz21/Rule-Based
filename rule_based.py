from experta import *

# Definisikan fakta
class CarProblem(Fact):
    pass

# Definisikan sistem pakar
class CarDiagnosis(KnowledgeEngine):

    @Rule(CarProblem(car_wont_start="yes", engine_cranks="no", lights_work="no"))
    def dead_battery(self):
        print("Diagnosis: Battery is dead")

    @Rule(CarProblem(car_wont_start="yes", engine_cranks="yes", fuel_level="empty"))
    def refuel_needed(self):
        print("Diagnosis: Refuel the car")

    @Rule(CarProblem(car_wont_start="yes", engine_cranks="yes", fuel_level=MATCH.fuel_level), 
          TEST(lambda fuel_level: fuel_level != "empty"))
    def ignition_or_fuel_system_problem(self):
        print("Diagnosis: Problem with ignition or fuel system")

    @Rule(CarProblem(car_wont_start="no"))
    def no_issue_detected(self):
        print("Diagnosis: No issues detected")

    @Rule(NOT(CarProblem(car_wont_start=W())))
    def insufficient_data(self):
        print("Diagnosis: Insufficient data for diagnosis")


# Jalankan sistem
if __name__ == "__main__":
    engine = CarDiagnosis()
    engine.reset()  # Reset sistem pakar
    
    # Masukkan fakta
    engine.declare(CarProblem(
        car_wont_start="yes",
        engine_cranks="yes",
        lights_work="no",
        battery_age="old",
        fuel_level="empty"
    ))

    engine.run()  # Jalankan inference
