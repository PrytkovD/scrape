package org.example.repository;

import org.example.model.YoutubeReactionEntity;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface YoutubeReactionRepository extends JpaRepository<YoutubeReactionEntity, Long> {

    Optional<YoutubeReactionEntity> findById(long id);
}
