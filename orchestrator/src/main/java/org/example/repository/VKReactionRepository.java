package org.example.repository;

import org.example.model.VKReactionEntity;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface VKReactionRepository extends JpaRepository<VKReactionEntity, Long> {

    Optional<VKReactionEntity> findById(long id);
}
