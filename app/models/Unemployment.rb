class Unemployment

  def initialize
    @json = JSON.parse(File.read(Rails.root.join("./data/input/tier_4_unemployment.json")))
  end

  def title
    @json["title"]
  end

  def blurb_paragraphs
    @json["description"]
  end

  def context_paragraphs
    @json["context"]
  end

  def analysis_paragraphs
    @json["analysis"]
  end

  def source_title
    @json["source"]["title"]
  end

  def source_link
    @json["source"]["link"]
  end

  def date
    @json["date"]
  end

end
