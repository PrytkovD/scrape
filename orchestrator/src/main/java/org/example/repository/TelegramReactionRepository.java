package org.example.repository;

import org.example.model.TelegramReactionEntity;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface TelegramReactionRepository extends JpaRepository<TelegramReactionEntity, Long> {

    Optional<TelegramReactionEntity> findById(long id);
}
