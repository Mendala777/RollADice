while True:
  print("Type 'r' for roll a dice")
  if input() == "r":
    import random
    rng=(random.randint(1,6)) 
    # print(rng)
  if rng == 1:
    print("""
        ┌─────────┐
        │         │
        │    ●    │
        │         │
        └─────────┘""") 
  if rng == 2:
    print("""
        ┌─────────┐
        │  ●      │
        │         │
        │      ●  │
        └─────────┘""")
  if rng ==3:
    print(""" 
        ┌─────────┐
        │  ●      │
        │    ●    │
        │      ●  │
        └─────────┘""")
  if rng ==4:
    print("""
        ┌─────────┐
        │  ●   ●  │
        │         │
        │  ●   ●  │
        └─────────┘""")
  if rng ==5:
    print("""
        ┌─────────┐
        │  ●   ●  │
        │    ●    │
        │  ●   ●  │
        └─────────┘""")
  if rng ==6:
    print("""
        ┌─────────┐
        │  ●   ●  │
        │  ●   ●  │
        │  ●   ●  │
        └─────────┘""")