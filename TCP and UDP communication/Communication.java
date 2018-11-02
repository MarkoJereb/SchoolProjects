/**
 * 1. domača naloga pri predmetu Računalniška omrežja
 *
 * Cilj: Na osnovi opisa delovanja implementirati odjemalski in strežniški program v programskem jeziku JAVA,
 * ki uporabljata protokola UDP in TCP za komunikacijo na transportni plasti.
 * V prvem delu izvajanja kode odjemalca in strežnika poteka UDP komunikacija.
 * V drugem delu izvajanja kode odjemalca in strežnika poteka TCP komunikacija.
 * Zaradi lažjega sledenja toka programiranja izvorno kodo obvezno dokumentirajte z uporabo komentarjev. *
 *
 * Avtor: Marko Jereb
 * */

import java.io.*;
import java.net.*;

public class Communication
{
   public int lineCount;
   public int numWords = 0;

    public static void main(String[] args) throws Exception
    {
	    // Start with communication
       System.out.println("Začenjam comunikacijo UDP ...");
       new Communication().udpCommunication();
       Thread.sleep(5000);
       System.out.println("***");
       System.out.println("***");
       System.out.println("***");
       System.out.println("Začenjam komunikacijo TCP ...");
       new Communication().tcpCommunication();

    }

   public void udpCommunication () throws Exception
    {
       // create URL object
       URL urlSite = new URL("https://www.fis.unm.si/");
       //create URL reader
       BufferedReader input = new BufferedReader(
          new InputStreamReader(urlSite.openStream()));
       //read input and count words in each line
       String inputLine;
       while ((inputLine = input.readLine()) != null)
       {
          lineCount++;

       }
       //close reader
       input.close();

       // create writer object
       BufferedWriter writer = null;
       try
       {
          // create .txt file and write number of lines on web page
          File txtFile = new File("vsebina.txt");
          writer = new BufferedWriter(new FileWriter(txtFile));
          writer.write(Integer.toString(lineCount));
       }
       catch (Exception e)
       {
          e.printStackTrace();
       }
       finally
       {
         try
         {
            // close writer regardless of what happens
            writer.close();
         }
         catch (Exception e){} // empty catch
       }
       System.out.printf("Povezal sem se na URL" +
          " naslov, prebral sem vsebino in jo shranil v datoteko. Stevilo vrstic je: %d%n", lineCount);
       System.out.println("Pošiljam podatke UDP strežniku ter čakam na odgovor.");
       new UDPServer().runServer(2227);
       new UDPClient().runClient(lineCount, "localhost", 2227);
    }

    public void tcpCommunication() throws IOException
    {
       int words = countWords();

       System.out.println("Iz datoteke smo prebrali " + Integer.toString(words) + " besed.");
       new TCPServer().runServer(2228);
       new TCPClient().runClient("localhost", 2228, words);
    }

    // read number of words in text file
    public int countWords() throws IOException
    {
       try
       {
          // open file and count all word in text file
          File file = new File("xanadu.txt");
          FileInputStream fileStream = new FileInputStream(file);
          InputStreamReader input = new InputStreamReader(fileStream);
          BufferedReader reader = new BufferedReader(input);
          String textLine;

          while ((textLine = reader.readLine()) != null)
          {
             String []words = textLine.split("\\s+");
             numWords += words.length;
          }
          fileStream.close();
       }
       catch (Exception e){}

       return numWords;
    }
} // end Class Communication
