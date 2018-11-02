/**
 * Razred UDPClient.
 */

import java.io.*;
import java.net.*;
import java.nio.ByteBuffer;

public class UDPClient
{
    public void runClient(int count, String server, int port) throws IOException
    {
        (new Thread()
        {
            @Override
            public void run()
            {
                try {
                    // create socket with server
                    DatagramSocket clientSocket = new DatagramSocket();
                    InetAddress IPAddress = InetAddress.getByName(server);

                    // send data to server
                    byte[] sendBuffer = ByteBuffer.allocate(4).putInt(count).array(); // convert int to byte array
                    DatagramPacket sendPacket = new DatagramPacket(
                       sendBuffer, sendBuffer.length, IPAddress, port);
                    clientSocket.send(sendPacket);

                    // receive data from server
                    while (true)
                    {
                        byte[] receiveBuffer = new byte[1024];
                        DatagramPacket receivedPacket = new DatagramPacket(
                           receiveBuffer, receiveBuffer.length);
                        clientSocket.setSoTimeout(10000); // socket time out 10s

                        try
                        {
                            clientSocket.receive(receivedPacket);
                            String receivedData = new String(receivedPacket.getData(), 0, receivedPacket.getLength());
                            // System.out.println("Nazaj sem dobil: " + receivedData);

                            if (receivedData.equals("10"))
                            {
                                System.out.println("Prejel sem potrdilno sporočilo in s tem UDP" +
                                   " odjemalec zaključuje z delovanjem.");
                                break;
                            }
                        }
                        catch (SocketTimeoutException ste)
                        {
                            System.out.println("Potekel je zahtevek za sprejem");
                        }
                        Thread.sleep(200);
                    }
                    clientSocket.close();
                }
                catch (UnknownHostException ex) {
                    System.out.println("Naslova ne morem razrešiti na IP");
                }
                catch (IOException ex) {
                    System.out.println(ex);
                }
                catch (InterruptedException e){
                    e.printStackTrace();
                }
            }
        }).start();
    }
} // end Class UDPClient
