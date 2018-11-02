/**
 * Razred TCPServer
 */

import java.net.*;
import java.io.*;


public class TCPServer
{
    public void runServer(int lport) throws IOException
    {
       (new Thread()
       {
          public void run()
          {
             // Create TCP server socket
             ServerSocket serverSocket = null;
             try {
                serverSocket = new ServerSocket(lport);
             }
             catch (IOException e) {
                System.out.println("Nisem mogel zasesti vrat" + lport);
                System.exit(1);
             }
             // System.out.println("Cakam ...");

             // Accept client
             Socket clientSocket = null;
             try {
                clientSocket = serverSocket.accept();
             }
             catch (IOException e) {
                System.out.println("Nisem mogel dobiti povezave");
                System.exit(1);
             }

             System.out.println("Povezan, čakam na promet.");
             try
             {
                BufferedReader in = new BufferedReader(
                   new InputStreamReader(
                      clientSocket.getInputStream()));
                PrintWriter out = new PrintWriter(
                   clientSocket.getOutputStream(), true);

                // First stream of communication
                String inputLine = in.readLine().replace("\n", "").replace("\r", ""); // read message
                int firstNum = Integer.parseInt(inputLine);
                System.out.println("Prejel sem podatke. Število besed v datoteki je " + inputLine);
                out.println("11"); // send message
                // System.out.println("Sporočilo poslano.");

                // Second stream of communication
                String inputLine2 = in.readLine().replace("\n", "").replace("\r", ""); // first message
                int secondNum = Integer.parseInt(inputLine2);
                String inputLine3 = in.readLine().replace("\n", "").replace("\r", ""); // second message
                int thirdNum = Integer.parseInt(inputLine3);
                System.out.println("Prejel sem število " + inputLine2 + ", vneseno preko tipkovnice.");
                int sumOFNumbers = firstNum + secondNum + thirdNum;
                out.println(Integer.toString(sumOFNumbers)); // send message

                // Close all streams
                in.close();
                out.close();
                clientSocket.close();
                serverSocket.close();
             }
             catch (IOException e){}
          }
       }).start();
    }
} // end class TCPServer
