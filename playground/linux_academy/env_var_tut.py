# set in linux env variable STAGE
# STAGE = staging


import os

#stage = os.environ["STAGE"].upper()
stage = os.getenv("STAGE", default = 'dev').upper()


output = f"We're running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output
elif stage.startswith("DEV"):
    output = "We're running on DEV "

print(output)

