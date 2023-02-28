package org.example.repository;

import org.example.model.BloggerEntity;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface BloggerRepository extends JpaRepository<BloggerEntity, Long> {
    Optional<BloggerEntity> findById(long id);
}
