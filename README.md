# Hospital Segment

## Overview
This project implements a small section of a medical app where patient data is made available to doctors such that
caregivers can be assigned to them if need be and prescriptions can equally be given to them. 

This project is hosted [here.](https://hospital-segment.onrender.com)

## Setup

* Runtime: Python 3.12
* OS: Windows | Linux | Mac
* Technologies used:
  1. [x] Flask
  2. [x] SQLAlchemy
  3. [x] Marshmallow

_For local setup_
```shell
cd ~
git clone https://github.com/Mimi97-aqua/hospital_segment.git
cd hospital_segment
pip install -r requirements,txt
```

## Implementation

Based on the Figma design, the database required 3 main objects (tables), namely:
- Participant 
- Prescriptions
- Care Giver

From here, I proceeded to implementing the API routes.

### API Docs
- View documentation (here.)[https://github.com/Mimi97-aqua/hospital_segment/blob/main/API_DOCS.md]
- To test out the APIs, visit this link to view the [Postman collection.](https://lunar-satellite-35635.postman.co/workspace/My-Workspace~74c77565-9011-4541-82dc-8d69a497f4db/collection/33878300-d1faaabe-c978-4e38-a34e-0956c09b43af?action=share&creator=33878300)
