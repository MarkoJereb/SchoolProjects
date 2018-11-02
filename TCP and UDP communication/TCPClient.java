/**
 * razred TCPClient
 */

import java.net.*;
import java.io.*;

public class TCPClient
{
    public void runClient(String server, int sport, int wordCount) throws IOException
    {
       (new Thread()
       {
          public void run()
          {
             // create new TCP client socket
             Socket clientSocket = null;
             try {
                clientSocket = new Socket(server, sport);

             }
             catch (UnknownHostException e) {
                System.out.println("Ne morem razresiti domene");
                System.exit(1);
             }
             catch (IOException e) {
                System.out.println("Ne morem se povezati na streznik");
                System.exit(1);
             }

             // server communication
             try
             {
                BufferedReader in = new BufferedReader(
                   new InputStreamReader(
                      clientSocket.getInputStream())); // create buffer reader
                PrintWriter out = new PrintWriter(
                   clientSocket.getOutputStream(), true); // create writer


                // Send first message (number of words in .txt file)
                out.println(Integer.toString(wordCount));
                String inputLine = in.readLine();
                System.out.println(inputLine);
                String read = inputLine.replace("\n", "").replace("\r", "");
                if (read.equals("11"))
                   System.out.println("“Prejel sem potrdilno sporočilo.");

                // Get input from user (integer)
                BufferedReader userInput = new BufferedReader(
                   new InputStreamReader(System.in));
                System.out.print("Vnesite celo število: ");
                String line = userInput.readLine().replace("\n", "").replace("\r", ""); // users input
                System.out.println("Vneseno število je: " + line);
                out.println(line); // send data

                // Get text data from txt. file
                try
                {
                   File file = new File("vsebina.txt");
                   FileInputStream fileStream = new FileInputStream(file);
                   InputStreamReader input = new InputStreamReader(fileStream);
                   BufferedReader reader = new BufferedReader(input);
                   String textLine = reader.readLine().replace("\n", "").replace("\r", "");
                   out.println(textLine);
                   fileStream.close();
                }
                catch (Exception e ){}

                // Read message from server
                String lastMessage = in.readLine().replace("\n", "").replace("\r", "");
                System.out.println("Seštevek, ki ga je podal strežnik je: " + lastMessage);

                // Close all streams
                out.close();
                in.close();
                //stdIn.close();
                clientSocket.close();}
             catch (IOException e){}
          }
       }).start();
    }
} // end Class TCPClient