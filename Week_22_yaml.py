from inventory_1 import inventory
import yaml

# CONVERT INVENTORY TO YAML AND WRITE TO FILE
with open("inventory.yaml", "w") as yaml_out:
    yaml_out.write(yaml.dump(inventory))

# READ YAML INVENTORY FROM FILE
with open("inventory.yaml", "r") as yaml_in:
    yaml_inventory = yaml_in.read()

# PRINT YAML INVENTORY STRING
print("inventory.yaml file:\n", yaml_inventory)

# CONVERT YAML INVENTORY TO PYTHON, THEN CONVERT BACK TO STRING FOR PRINTING
print("\nyaml pretty version:")
print(yaml.dump(yaml.safe_load(yaml_inventory), indent=4))

# COMPARE INVENTORY WE READ, WITH ORIGINAL INVENTORY, TO MAKE SURE THEY ARE EQUIVALENT
print("\n----- compare saved inventory with original --------------------")
saved_inventory = yaml.safe_load(yaml_inventory)
if saved_inventory == inventory:
    print("-- worked: saved inventory equals original")
else:
    print("-- failed: saved inventory different from original")
    
    
# READ THE ALT-FORMATTED YAML FILE
with open("inventory_formatted.yaml", "r") as yaml_in:
    yaml_inventory_alt = yaml_in.read()
    
print("\n\ninventory_formatted.yaml file:")
print(yaml_inventory_alt)

# COMPARE INVENTORY WE READ, WITH ORIGINAL INVENTORY, TO MAKE SURE THEY ARE EQUIVALENT
print("\n----- compare saved inventory with original --------------------")
saved_inventory_alt = yaml.safe_load(yaml_inventory_alt)
if saved_inventory_alt == inventory:
    print("-- worked: saved alt-formatted inventory equals original")
else:
    print("-- failed: saved alt-formatted inventory different from original")
