package com.amanpati.backend;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/internships")
public class InternshipController {

    @Autowired
    private InternshipRepository internshipRepository;

    // Nai internship add karo
    @PostMapping
    public Internship createInternship(
            @RequestBody Internship internship) {
        return internshipRepository.save(internship);
    }

    // Saari internships dekho
    @GetMapping
    public List<Internship> getAllInternships() {
        return internshipRepository.findAll();
    }

    // Ek internship dekho ID se
    @GetMapping("/{id}")
    public Internship getInternship(
            @PathVariable String id) {
        return internshipRepository.findById(id)
                .orElse(null);
    }

    // Internship delete karo
    @DeleteMapping("/{id}")
    public String deleteInternship(
            @PathVariable String id) {
        internshipRepository.deleteById(id);
        return "Internship deleted!";
    }
}
