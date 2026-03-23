import arrow

brewing_time = arrow.utcnow()   # current UTC time

# Timezone convert karo
rome_time = brewing_time.to("Europe/Rome")

from collections import namedtuple

# Define karo — tuple ka naam aur fields
ChaiProfile = namedtuple("ChaiProfile", ["flavor", "aroma", "color"])

# Use karo
my_chai = ChaiProfile(flavor="spicy", aroma="strong", color="brown")
print(my_chai.flavor)   # spicy — naam se access karo, index se nahi