import fastf1
fastf1.Cache.enable_cache('/Volumes/GoogleDrive-104137785854558514229/My Drive/Cornell Sophomore Year/Semester 4/ORIE 3120/Project')  
session = fastf1.get_session(2019, 'Monza', 'Q')
session.load(telemetry=False, laps=False, weather=False)
vettel = session.get_driver('VET')
print(f"Pronto {vettel['FirstName']}?")