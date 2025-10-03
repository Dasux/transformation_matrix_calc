import numpy as np 

print("\n\n [=================== Transformation Matrix Calculator ===================]")

#=========================================================================
# Rotation Matrices (angles given in degrees)
def rot_x(theta_deg):
    theta = np.radians(theta_deg)   # convert to radians
    return np.array([
        [1, 0, 0, 0],
        [0, round(np.cos(theta), 2), -round(np.sin(theta), 2), 0],
        [0, round(np.sin(theta), 2), round(np.cos(theta), 2), 0],
        [0, 0, 0, 1]
    ])

def rot_y(theta_deg):
    theta = np.radians(theta_deg)
    return np.array([
        [round(np.cos(theta), 2), 0, round(np.sin(theta), 2), 0],
        [0, 1, 0 , 0],
        [-round(np.sin(theta), 2), 0, round(np.cos(theta), 2), 0],
        [0, 0, 0, 1]
    ])

def rot_z(theta_deg):
    theta = np.radians(theta_deg)
    return np.array([
        [round(np.cos(theta), 2), -round(np.sin(theta), 2), 0, 0],
        [round(np.sin(theta), 2), round(np.cos(theta), 2), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

# Translation Matrices
def tran_x(d):
    return np.array([
        [1, 0, 0, d],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def tran_y(d):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, d],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def tran_z(d):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, d],
        [0, 0, 0, 1]
    ])
#=========================================================================

# =========================== [Matrix MULTIPLICATION] ===========================
n = int(input("enter number of transformations \n -> "))

I = np.eye(4)  # identity matrix

commands = []
print("\n enter the transformations (e.g. rx 90, ty 3):\n")
for i in range(1, n+1):
    commands.append(input(f"{i} ").lower()) # made it lower--- so that the command isnt case sensitive

    # one more thing i must add--- is a way for the user to be able to felxibly enter commands
    # which means "rx 30" should be the same as "rx30"
    # they shouldn't have to worry about spaces
    #
    # one approach is to just remove all spaces from the input string... but that is rash 
    # another approach is to check for alpha-numeric combinations and split them as the value of the command 
    # i can do it by extracting the first and last occurence of an alpha-num character--- and getting the index of that 
    # then i could just slice the string--- simple shit! 

    # im using a dictionary to map command prefixes to functions cause im lazy
operations = {
    "rx": rot_x,
    "ry": rot_y,
    "rz": rot_z,
    "tx": tran_x,
    "ty": tran_y,
    "tz": tran_z,
}

for i in commands:
    if i[:2] in operations:
        func = operations[i[:2]]
        value = int(i[3:])  # integer only
        I = np.dot(I, func(value))

# round final matrix for clean output
I = np.round(I, 2)
print("\nFinal Transformation Matrix:")
print(I)
