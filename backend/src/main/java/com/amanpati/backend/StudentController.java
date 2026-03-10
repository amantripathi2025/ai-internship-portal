package com.amanpati.backend;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/students")
public class StudentController {

    @Autowired
    private StudentRepository studentRepository;

    @PostMapping
    public Student createStudent(@RequestBody Student student) {
        return studentRepository.save(student);
    }

    @GetMapping
    public List<Student> getAllStudents() {
        return studentRepository.findAll();
    }

    @GetMapping("/{id}")
    public Student getStudent(@PathVariable String id) {
        return studentRepository.findById(id).orElse(null);
    }

    @DeleteMapping("/{id}")
    public String deleteStudent(@PathVariable String id) {
        studentRepository.deleteById(id);
        return "Student deleted!";
    }
}