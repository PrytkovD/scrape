package org.example.rabbitlistener;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.example.dto.event.VKMessage;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
@Slf4j
public class VKListener {


    @RabbitListener(queues = {"${service-rabbit.vk-routing-key}"}, ackMode = "AUTO")
    public void getMessage(VKMessage message){
        log.info("VK: {}", message);
    }

}
