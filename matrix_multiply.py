import numpy as np
import os

# दोन मॅट्रिक्स तयार करा
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# मॅट्रिक्स मल्टिप्लिकेशन
result = np.dot(A, B)

# आउटपुट डिरेक्टरी तयार करा (जर नसेल तर)
os.makedirs('output', exist_ok=True)

# आउटपुट फाइलमध्ये सेव्ह करा
with open('output/output.txt', 'w') as f:
    f.write(str(result))
