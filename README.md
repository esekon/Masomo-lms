[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/SNqTfQzC)

# Student Portal

## Introduction

The student portal is designed to streamline administrative processes related to enrollments, payments, and student progress within courses. This portal aims to enhance the overall experience for both students and administrators by providing a user-friendly interface and efficient management tools.

## Objectives

- Develop a secure and user-friendly web-based portal for students and administrators.
- Implement features for easy enrollment management, allowing students to register for courses online.
- Integrate a payment system to facilitate secure transactions for course fees.
- Provide tools for tracking and monitoring student progress within enrolled courses.
- Ensure scalability and adaptability to accommodate future expansions and updates.

## Features

### User Management

- **Registration:** Students and administrators can create accounts with unique usernames and passwords.
- **Authentication:** Secure login process using username/email and password authentication mechanism.
- **User Roles:** Differentiate between student and administrator roles with distinct access permissions.

### Enrollment Management

- **Course Listings:** Display available courses with details such as course name, description, instructor, schedule, and enrollment status.
- **Enrollment Process:** Students can select courses, add them to their cart, and complete the enrollment process by making payment.
- **Enrollment Limits:** Set maximum enrollment limits for each course to prevent overbooking.

### Payment System

- **Payment Gateway Integration:** Integrate with Stripe API to process payments securely using credit/debit cards, online banking, and other payment methods.
- **Payment Notifications:** Send automatic notifications for payment due dates, payment confirmations, and reminders for pending payments.

### Progress Tracking

- **Course Progress:** Students can track their progress within enrolled courses, including completion status, grades, assignments, quizzes, and course materials.
- **Progress Reports:** Generate progress reports for individual students and courses, detailing performance metrics and areas for improvement.

### Communication Tools

- **Messaging System:** Provide a built-in messaging system for communication between students, instructors, and administrators.
- **Announcements:** Allow administrators to broadcast announcements, updates, and important information to all users.

## Security Requirements

- **Data Encryption:** Implement HTTPS encryption for secure data transmission over the network.
- **Authentication Security:** Implement password hashing and salting techniques to securely store user passwords.
- **Authorization:** Enforce role-based access control (RBAC) to restrict access to sensitive data and functionalities based on user roles.

## Performance Requirements

- **Response Time:** Aim for fast response times (<500ms) for page loads and API requests.
- **Scalability:** Design the system to handle a large number of concurrent users and course enrollments, with provisions for horizontal scaling.
- **Reliability:** Ensure high availability and uptime (>99%) through load balancing, fault tolerance, and disaster recovery measures.

## Deployment Requirements

- **Deployment Environment:** Deploy as a static web application and another web service for the API at render.

---