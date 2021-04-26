import csv


class Writer(object):

    def __init__(self, data, identifier):
        self.data = data
        self.id = identifier

    def _get_length(self):
        """
        Get the length of the data array

        :return: Number
        """
        return len(self.data)

    def save(self):
        """
        Write out the contents of the data into a CSV file

        :return: None
        """
        n = self._get_length()
        with open("%s_distogram.csv" % self.id, "w", newline='') as csv_output:
            writer = csv.writer(csv_output)
            # These are the expected headers
            writer.writerow(["residueA","residueB","distance"])
            for i in range(n):
                for j in range(n):
                    # Only write out distance values <20
                    # This is because the interactive data visualisation would break with too many data points
                    # Luckily, values >20 are meaningless in terms of usability and so can be safely removed
                    if self.data[i][j] < 20:
                        writer.writerow([i+1, j+1, "%.2f" % self.data[i][j]])
