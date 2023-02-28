package org.example.config;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.rabbitmq.client.Channel;
import lombok.RequiredArgsConstructor;
import org.springframework.amqp.rabbit.connection.Connection;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.amqp.support.converter.Jackson2JsonMessageConverter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Import;
import org.springframework.retry.backoff.FixedBackOffPolicy;
import org.springframework.retry.policy.SimpleRetryPolicy;
import org.springframework.retry.support.RetryTemplate;
import org.springframework.validation.Validator;
import org.springframework.validation.beanvalidation.OptionalValidatorFactoryBean;

@Configuration
@RequiredArgsConstructor
@Import(SomeRabbitBeansConfig.class)
public class MyRabbitConfig {
    private final RabbitTemplate template;
    private final ObjectMapper objectMapper;

    @Bean
    public RetryTemplate getRetryTemplate() {
        FixedBackOffPolicy fixedBackOffPolicy = new FixedBackOffPolicy();
        fixedBackOffPolicy.setBackOffPeriod(3000L);

        SimpleRetryPolicy retryPolicy = new SimpleRetryPolicy();
        retryPolicy.setMaxAttempts(3);

        RetryTemplate retryTemplate = new RetryTemplate();
        retryTemplate.setBackOffPolicy(fixedBackOffPolicy);
        retryTemplate.setRetryPolicy(retryPolicy);

        return retryTemplate;
    }

    @Bean
    public Connection getConnection() {
        return template.getConnectionFactory().createConnection();
    }

    @Bean
    public void configureRabbitTemplate() {
        template.setMessageConverter(new Jackson2JsonMessageConverter(objectMapper));
    }

    @Bean
    public Validator amqpValidator() {
        return new OptionalValidatorFactoryBean();
    }

    @Bean
    public Channel getChannel() {
        return getConnection().createChannel(false);
    }
}
