package com.amanpati.backend;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.List;

@Data
@Document(collection = "internships")
public class Internship {

    @Id
    private String id;
    private String title;
    private String company;
    private String location;
    private List<String> requiredSkills;
    private String stipend;
    private String duration;
    private String description;
    private String applyLink;
}