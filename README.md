# Custom Odoo Modules

This repository contains custom Odoo modules for managing hotels and students. Each module has been designed to handle specific business requirements effectively.

---

## Modules Overview

### 1. Hotel Management Module (`hotel_management`)
The `hotel_management` module provides features to manage hotels, rooms, bookings, and additional features.

#### Features:
- Manage hotels and their details.
- Manage rooms with their configurations.
- Handle bookings and customer reservations.
- Support for additional hotel features.

#### Module Structure:
- **Models**:
  - `booking.py`: Manages booking-related data and operations.
  - `feature.py`: Handles additional features of hotels.
  - `hotel.py`: Manages hotel information.
  - `room.py`: Handles room-related data.
- **Security**:
  - `ir.model.access.csv`: Access control for the module.
- **Views**:
  - `booking_views.xml`: Booking-related views.
  - `feature_views.xml`: Feature-related views.
  - `hotel_views.xml`: Hotel-related views.
  - `room_views.xml`: Room-related views.
  - `menu.xml`: Navigation menu for the module.

---

### 2. Student Management Module (`student_management`)
The `student_management` module allows you to manage students, their optional subjects, and related information.

#### Features:
- Manage student information, including enrollment status.
- Handle optional subjects for students.

#### Module Structure:
- **Models**:
  - `student_management.py`: Manages student-related data and operations.
  - `student_optional_subject.py`: Handles optional subject details for students.
- **Security**:
  - `ir.model.access.csv`: Access control for the module.
- **Views**:
  - `student_management_views.xml`: Student-related views.
  - `student_optional_subjects.xml`: Optional subject-related views.

---

## Getting Started

1. **Prerequisites**:
   - Ensure you have Odoo installed and configured.
   - Place the `hotel_management` and `student_management` directories inside the `addons` folder of your Odoo installation.

2. **Installation**:
   - Activate developer mode in Odoo.
   - Go to the Apps menu and click "Update Apps List".
   - Search for `hotel_management` or `student_management` and click "Install".

3. **Configuration**:
   - Assign appropriate user roles in the `ir.model.access.csv` file.

---

## Contribution

Feel free to contribute to these modules by submitting issues or pull requests.

---

## License

These modules are distributed under the [MIT License](https://opensource.org/licenses/MIT).

---

## Author

Developed by LeePT.

