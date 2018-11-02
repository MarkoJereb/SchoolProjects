/**
 * Razred UDPServer.
 */

import java.io.*;
import java.net.*;

public class UDPServer
{
    public void runServer(int lport) throws IOException
    {
       (new Thread()
       {
          @Override
          public void run()
          {
             // create UDP Socket
             try {
                DatagramSocket serverSocket = new DatagramSocket(lport);

                // Server listens and answers for unlimited time
                while (true)
                {
                   // receive data from client
                   byte[] receiveBuffer = new byte[1024];
                   DatagramPacket receiveData = new DatagramPacket(
                      receiveBuffer, receiveBuffer.length);
                   System.out.println("Cakam na paket na vratih: " + lport);
                   serverSocket.receive(receiveData);
                   String sentence = new String(receiveData.getData());
                   System.out.println("Prejel sem UDP paket z vsebino " + sentence + ".");

                   // send data to client
                   String message = "10";
                   byte[] sendBuffer = new byte[1024];
                   int port = receiveData.getPort();
                   InetAddress IPAddress = receiveData.getAddress();
                   // System.out.println("Sprejel paket iz " + IPAddress + ", vrata " + port);
                   // System.out.println("Sprejel vsebino: " + sentence);
                   sendBuffer = message.getBytes();
                   System.out.println("Posiljam potrditveno sporočilo UDP odjemalcu.");

                   DatagramPacket sendPacket = new DatagramPacket(
                      sendBuffer, sendBuffer.length, IPAddress, port);
                   serverSocket.send(sendPacket);
                   break;
                }
                serverSocket.close();
             }
             catch (SocketException ex) {
                System.out.println("UDP Port je zaseden.");
                System.exit(1);
             }
             catch (IOException e){
                e.printStackTrace();
             }
          }
       }).start();
    }
} // end Class UDPServer