package com.amanpati.backend;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface InternshipRepository
        extends MongoRepository<Internship, String> {
}