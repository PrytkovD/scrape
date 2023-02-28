package org.example.service;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class WhoisServiceHttpClientImpl implements WhoisService {
    @Override
    public String whois(String domainName) {
        try {
            URL url = new URL("localhost:8080/whois");
            String param = "?domain_name=" + domainName;

            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setConnectTimeout(0);
            connection.setReadTimeout(0);

            DataOutputStream out = new DataOutputStream(connection.getOutputStream());
            out.writeBytes(param);
            out.flush();
            out.close();

            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String inputLine;
            StringBuilder content = new StringBuilder();

            while ((inputLine = in.readLine()) != null) {
                content.append(inputLine);
            }

            in.close();

            connection.disconnect();

            return content.toString();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
